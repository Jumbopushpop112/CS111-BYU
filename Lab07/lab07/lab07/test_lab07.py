from PIL import Image as PILImage, ImageChops
from byu_pytest_utils import max_score, test_files, with_import
from pytest import approx, xfail
from pathlib import Path
import sys

sys.path.append(str(test_files))
import image_solutions  # nopep8


def compare_images(obs: Path | PILImage.Image, exp: Path | PILImage.Image):
    if not isinstance(obs, PILImage.Image):
        observed = PILImage.open(obs).convert('RGB')
    else:
        observed = obs
    if not isinstance(exp, PILImage.Image):
        expected = PILImage.open(exp).convert('RGB')
    else:
        expected = exp

    assert observed.size == expected.size, f"Image sizes don't match. Expected `{expected.size}`, but got `{observed.size}`."

    diff = ImageChops.difference(observed, expected)
    if bbox := diff.getbbox():
        for y in range(bbox[1], bbox[3]):
            for x in range(bbox[0], bbox[2]):
                observed_pixel = observed.getpixel((x, y))
                expected_pixel = expected.getpixel((x, y))
                if not observed_pixel or not expected_pixel:
                    assert False, f"Failed to get pixels at ({x}, {y})!"

                if isinstance(observed_pixel, (float, int)) or isinstance(expected_pixel, (float, int)):
                    assert False, "Failed to get correct pixel type!"

                assert observed_pixel[0] == approx(expected_pixel[0], abs=2), f"The pixels' red values at ({x}, {y}) don't match. Expected `{expected_pixel[0]}`, but got `{observed_pixel[0]}`."
                assert observed_pixel[1] == approx(expected_pixel[1], abs=2), f"The pixels' green values at ({x}, {y}) don't match. Expected `{expected_pixel[1]}`, but got `{observed_pixel[1]}`."
                assert observed_pixel[2] == approx(expected_pixel[2], abs=2), f"The pixels' blue values at ({x}, {y}) don't match. Expected `{expected_pixel[2]}`, but got `{observed_pixel[2]}`."

    if isinstance(obs, Path):
        obs.unlink(missing_ok=True)


@max_score(3)
@with_import('lab07', 'iron_puzzle')
def test_iron_puzzle(iron_puzzle):
    observed = iron_puzzle(test_files / 'iron.png')
    compare_images(observed.image, image_solutions.iron_solution)


@max_score(3)
@with_import('lab07', 'west_puzzle')
def test_west_puzzle(west_puzzle):
    observed = west_puzzle(test_files / 'west.png')
    compare_images(observed.image, image_solutions.west_solution)


@max_score(3)
@with_import('lab07', 'darken')
def test_darken(darken):
    observed = darken(test_files / 'cougar.png', 0.8)
    compare_images(observed.image, test_files / 'cougar_darkened.key.png')


@max_score(3)
@with_import('lab07', 'grayscale')
def test_grayscale(grayscale):
    observed = grayscale(test_files / 'cougar.png')
    compare_images(observed.image, test_files / 'cougar_grayscale.key.png')


@max_score(3)
@with_import('lab07', 'sepia')
def test_sepia(sepia):
    observed = sepia(test_files / 'cougar.png')
    compare_images(observed.image, test_files / 'cougar_sepia.key.png')


@max_score(5)
@with_import('lab07', 'create_left_border')
def test_create_left_border(create_left_border):
    observed = create_left_border(test_files / 'cougar.png', 25)
    compare_images(observed.image, test_files / 'cougar_bordered.key.png')

@max_score(0)
def test_create_stripes():
    try:
        @with_import('lab07', 'create_stripes')
        def inner_create_stripes(create_stripes):
            observed = create_stripes(test_files / 'cougar.png')
            compare_images(observed.image, image_solutions.striped_solution)
        inner_create_stripes()
    except Exception as e:
        xfail(f'\nOPTIONAL: create_stripes() is not implemented correctly:\n{e}')

@max_score(0)
def test_copper_puzzle():
    try:
        @with_import('lab07', 'copper_puzzle')
        def inner_copper_puzzle(copper_puzzle):
            observed = copper_puzzle(test_files / 'cougar.png')
            compare_images(observed.image, image_solutions.copper_solution)
        inner_copper_puzzle()
    except Exception as e:
        xfail(f'\nOPTIONAL: copper_puzzle() is not implemented correctly:\n{e}')
