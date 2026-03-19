from byu_pytest_utils import max_score, with_import, dialog, test_files, this_folder, tier
try:
    from byu_pytest_utils.popup import set_popup
except ImportError:
    # Older version: popup module or method doesn't exist
    pass
else:
    set_popup(True)

core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)

@core
@max_score(0)
@with_import('task', 'Task')
def test_CORE_add_subtask(Task):
    main_task = Task('homework')
    subtask1 = Task('cs111')
    subtask2 = Task('math213')
    subtask3 = Task('cs180')
    subtask11 = Task('project4')
    subtask12 = Task('study for final')

    subtask1.add_subtask(subtask11)
    assert subtask1.subtasks == [subtask11]

    main_task.add_subtask(subtask1)
    main_task.add_subtask(subtask2)
    main_task.add_subtask(subtask3)
    subtask1.add_subtask(subtask12)

    assert [subtask1, subtask2, subtask3] == main_task.subtasks
    assert [subtask11, subtask12] == subtask1.subtasks
    assert not subtask2.subtasks
    assert not subtask3.subtasks

@core
@max_score(0)
@dialog(test_files / "test_CORE_ui_exit.dialog.txt", this_folder / "todo_list.py")
def test_CORE_ui_exit():
    ...

@core
@max_score(0)
@dialog(test_files / "test_CORE_ui_main_task.dialog.txt", this_folder / "todo_list.py")
def test_CORE_ui_main_task():
    ...

@advanced
@max_score(0)
@with_import('task', 'Task')
def test_ADVANCED_task_str(Task):
    main_task = Task('Take care of the cats')
    assert str(main_task) == 'Take care of the cats\n'

    subtask1 = Task('Feed them')
    main_task.add_subtask(subtask1)
    subtask2 = Task('Empty the litter box')
    main_task.add_subtask(subtask2)
    assert str(main_task) == 'Take care of the cats\n    Feed them\n    Empty the litter box\n'

    subtask11 = Task('Breakfast')
    subtask1.add_subtask(subtask11)
    subtask12 = Task('Lunch')
    subtask1.add_subtask(subtask12)
    subtask13 = Task('Dinner')
    subtask1.add_subtask(subtask13)
    assert str(main_task) == ('Take care of the cats\n    Feed them\n        Breakfast\n        Lunch\n' +
            '        Dinner\n    Empty the litter box\n')

    subtask111 = Task('Prepare food')
    subtask11.add_subtask(subtask111)
    subtask1111 = Task('Buy food')
    subtask111.add_subtask(subtask1111)
    assert str(main_task) == ('Take care of the cats\n    Feed them\n        Breakfast\n' +
            '            Prepare food\n                Buy food\n' +
            '        Lunch\n        Dinner\n    Empty the litter box\n')

@advanced
@max_score(0)
@dialog(test_files / "test_ADVANCED_ui_subtasks.dialog.txt", this_folder / "todo_list.py")
def test_ADVANCED_ui_subtasks():
    ...

@advanced
@max_score(0)
@dialog(test_files / "test_ADVANCED_ui_long.dialog.txt", this_folder / "todo_list.py")
def test_ADVANCED_ui_long():
    ...

@excellent
@max_score(0)
@dialog(test_files / "test_EXCELLENT_ui_errors.dialog.txt", this_folder / "todo_list.py")
def test_EXCELLENT_ui_errors():
    ...
