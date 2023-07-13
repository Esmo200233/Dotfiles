from libqtile import bar, widget
from libqtile.config import Screen
import os

# Default widgets style
widget_defaults = dict(
    opacity=1,
    font='monospace',
    fontsize=14,
    padding=0,
)

screens = [
    Screen(
        wallpaper=os.environ['XDG_PICTURES_DIR'] + '/Wallpaper.png',
        # How this image is painted to the screen is specified by the
        # `wallpaper_mode` parameter.
        # 'fill': Image will be centred on the screen and resized to fill it.
        # 'stretch': Image is stretched to fit all of it into the screen.
        wallpaper_mode='fill',
        bottom=bar.Bar(
            [
                # A list of available widgets that can found on ->
                # https://docs.qtile.org/en/latest/manual/ref/widgets.html

                # Display the icon represent current layout of current group.
                widget.CurrentLayoutIcon(),
                # Workspaces laybel
                widget.GroupBox(
                    highlight_method='line',
                    rounded=False,
                    hide_unused=True,
                    disable_drag=False,
                    use_mouse_wheel=True
                ),
                # A notify widget
                widget.Notify(
                    fmt=' 💬 {} ',
                    fontsize=15,
                    action=False,
                ),
                # Just an empty space on the bar.
                widget.Spacer(),
                # A widget that manages system tray.
                widget.Systray(),
                # Widget that display and change volume.
                widget.Volume(fmt=' 🔊 {} |'),
                # Widget to show the current brightness of a monitor.
                widget.Backlight(
                    backlight_name='intel_backlight',
                    format=' ☀️ {percent:1.0%} |',
                ),
                # Battery monitoring widget.
                widget.Battery(
                    format=' {char} {percent:2.0%} ',
                    notify_below=30,
                    discharge_char='🔋',
                    charge_char='⚡',
                    full_char='🔌',
                    empty_char='',
                    unknown_char='',
                    show_short_text=False
                ),
                # Displays memory/swap usage
                widget.Memory(
                    format='| 📊{MemUsed: .0f}MB |',
                ),
                # Displays net speed
                widget.Net(
                    interface='wlo1',
                    format=' {down} 🔻🔺 {up} '
                ),
                # Displays clock
                widget.Clock(
                    format='| 📅 %Y-%b-%d %a | 🕒 %H:%M%p '
                ),
                # Shows number of pending updates
                # widget.CheckUpdates(
                #     display_format=' ⬆️ {updates} Updates ',
                #     background=,
                #     distro=Commands.distribution,
                # ),
            ],
            25,
        ),
        # A gap placed along one of the edges of the screen.
        left=bar.Gap(size=6),
        right=bar.Gap(size=6),
        top=bar.Gap(size=6)
    ),
]
