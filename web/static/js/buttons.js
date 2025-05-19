function update_main_font_size() {
    var selector = document.getElementById('select_main_font_size');
    var size = selector.options[selector.selectedIndex].value;
    source.style.fontSize = size+"em";
    output_window.style.fontSize = size+"em";
}

function clear_runner() {
    var runner = document.getElementById('runner');
    runner.value = "";
}

function clear_source() {
    source.value = "";
}

function clear_local_source() {
    save(source.id+"_value", "");
}

function print_history() {
    var runner = document.getElementById('runner');
    runner.value = "--history--";
    document.getElementById('main_form').submit();
}

function focus_source() {
    var source_window = document.getElementById('source_window');
    source_window.style.width = "100vw";
    save(source_window.id+"_width", source_window.offsetWidth+"px");
}

function evenly_space_windows() {
    var source_window = document.getElementById('source_window');
    source_window.style.width = "49vw";
    save(source_window.id+"_width", source_window.offsetWidth+"px");
}

function focus_output() {
    var source_window = document.getElementById('source_window');
    source_window.style.width = "0vw";
    save(source_window.id+"_width", source_window.offsetWidth+"px");
}

function change_page_zoom() {
    var slider = document.getElementById("zoom_slider");
    var html = document.getElementsByTagName("html")[0];
    html.style.fontSize = slider.value+"em";
    save("page_zoom", slider.value);
}

function run() {
    save(source.id+'_value', source.value);
    document.getElementById('main_form').submit();
}

function toggle_console() {
    var console = document.getElementById("console");
    var console_menu = document.getElementById("console_menu");
    if (window.getComputedStyle(console, null).display === "none") {
        console.style.display = "block";
        console_menu.style.marginTop = "0";
        console_menu.style.background = "black";
    } else {
        console.style.display = "none";
        console_menu.style.marginTop = "auto";
        console_menu.style.background = "inherit";
    }
}
