from byu_pytest_utils import max_score, run_python_script, test_files, this_folder, ensure_missing, dialog, tier
from PIL import Image as PILImage, ImageChops
from pathlib import Path
from pytest import approx

core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)

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

@core
@ensure_missing(this_folder / 'launch_sites.output.png')
@max_score(0)
def test_CORE_site_launches():
    run_python_script(this_folder / 'orbital_launches.py')
    compare_images(this_folder / 'launch_sites.output.png', test_files / 'launch_sites.key.png')

@advanced
@ensure_missing(this_folder / 'countries.output.png')
@max_score(0)
def test_ADVANCED_country_launches():
    run_python_script(this_folder / 'orbital_launches.py')
    compare_images(this_folder / 'countries.output.png', test_files / 'countries.key.png')

@excellent
@max_score(0)
@dialog(test_files / "test_EXCELLENT_missing_sites.dialog.txt", this_folder / "orbital_launches.py")
def test_EXCELLENT_missing_sites():
    ...
