from make_todo_progress import MakeTodoProgress


def get_todo_progress(path):
    make_graph_todo_progress = MakeTodoProgress()

    make_graph_todo_progress.set_path_of_display_todo(path)
    todo_info = make_graph_todo_progress.get_todo_info()

    todo_start_time_series = todo_info.query("status == 'start'")["timestamp"]
    todo_stop_time_series = todo_info.query("status == 'stop'")["timestamp"]

    return make_graph_todo_progress.get_delta_datetime_list(todo_start_time_series, todo_stop_time_series)
