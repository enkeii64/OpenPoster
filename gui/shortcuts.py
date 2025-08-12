from __future__ import annotations

from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtCore import Qt


def setup_shortcuts(mw) -> None:
    for shortcut_item in mw.shortcuts_list:
        try:
            shortcut_item.setEnabled(False)
            shortcut_item.activated.disconnect()
        except Exception:
            pass
    mw.shortcuts_list.clear()

    settings_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.Preferences), mw)
    settings_shortcut.activated.connect(mw.showSettingsDialog)
    mw.shortcuts_list.append(settings_shortcut)

    open_file_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.Open), mw)
    open_file_shortcut.activated.connect(mw.openFile)
    mw.shortcuts_list.append(open_file_shortcut)

    export_shortcut_str = mw.config_manager.get_export_shortcut()
    if export_shortcut_str:
        export_shortcut = QShortcut(QKeySequence(export_shortcut_str), mw)
        export_shortcut.activated.connect(mw.exportFile)
        mw.shortcuts_list.append(export_shortcut)

    zoom_in_shortcut_str = mw.config_manager.get_zoom_in_shortcut()
    if zoom_in_shortcut_str:
        zoom_in_shortcut = QShortcut(QKeySequence(zoom_in_shortcut_str), mw)
        zoom_in_shortcut.activated.connect(mw.zoomIn)
        mw.shortcuts_list.append(zoom_in_shortcut)

    zoom_out_shortcut_str = mw.config_manager.get_zoom_out_shortcut()
    if zoom_out_shortcut_str:
        zoom_out_shortcut = QShortcut(QKeySequence(zoom_out_shortcut_str), mw)
        zoom_out_shortcut.activated.connect(mw.zoomOut)
        mw.shortcuts_list.append(zoom_out_shortcut)

    close_window_shortcut_str = mw.config_manager.get_close_window_shortcut()
    if close_window_shortcut_str:
        close_window_shortcut = QShortcut(QKeySequence(close_window_shortcut_str), mw)
        close_window_shortcut.activated.connect(mw.close)
        mw.shortcuts_list.append(close_window_shortcut)

    play_pause_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Space), mw)
    play_pause_shortcut.activated.connect(mw.toggleAnimations)
    mw.shortcuts_list.append(play_pause_shortcut)

    delete_layer_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Delete), mw)
    delete_layer_shortcut.activated.connect(mw.delete_selected_layer)
    mw.shortcuts_list.append(delete_layer_shortcut)
