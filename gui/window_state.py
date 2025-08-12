from __future__ import annotations

# splitter sizes
def apply_default_sizes(mw) -> None:
    if hasattr(mw, "ui") and hasattr(mw.ui, "mainSplitter"):
        total_width = mw.ui.mainSplitter.width()
        section_width = total_width // 3 if total_width else 1
        mw.ui.mainSplitter.setSizes([section_width, section_width, section_width])

    if hasattr(mw, "ui") and hasattr(mw.ui, "layersSplitter"):
        total_height = mw.ui.layersSplitter.height()
        section_height = total_height // 2 if total_height else 1
        mw.ui.layersSplitter.setSizes([section_height, section_height])


def save_splitter_sizes(mw) -> None:
    if hasattr(mw, "ui") and hasattr(mw.ui, "mainSplitter"):
        sizes = mw.ui.mainSplitter.sizes()
        mw.config_manager.save_splitter_sizes("mainSplitter", sizes)

    if hasattr(mw, "ui") and hasattr(mw.ui, "layersSplitter"):
        sizes = mw.ui.layersSplitter.sizes()
        mw.config_manager.save_splitter_sizes("layersSplitter", sizes)


def load_splitter_sizes(mw) -> None:
    if hasattr(mw, "ui") and hasattr(mw.ui, "mainSplitter"):
        sizes = mw.config_manager.get_splitter_sizes("mainSplitter")
        if sizes:
            mw.ui.mainSplitter.setSizes(sizes)

    if hasattr(mw, "ui") and hasattr(mw.ui, "layersSplitter"):
        sizes = mw.config_manager.get_splitter_sizes("layersSplitter")
        if sizes:
            mw.ui.layersSplitter.setSizes(sizes)


# window geometry
def load_window_geometry(mw) -> None:
    geometry = mw.config_manager.get_window_geometry()
    if geometry.get("remember_size"):
        size = geometry.get("size") or [mw.width(), mw.height()]
        pos = geometry.get("position") or [mw.x(), mw.y()]
        mw.resize(size[0], size[1])
        mw.move(pos[0], pos[1])
        if geometry.get("maximized"):
            mw.showMaximized()


def save_window_geometry(mw) -> None:
    if mw.isMaximized():
        ng = mw.normalGeometry()
        size = [ng.width(), ng.height()]
        position = [ng.x(), ng.y()]
        mw.config_manager.save_window_geometry(size, position, True)
    else:
        size = [mw.width(), mw.height()]
        position = [mw.x(), mw.y()]
        mw.config_manager.save_window_geometry(size, position, False)
