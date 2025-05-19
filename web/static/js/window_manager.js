// CREDITS for most of this:
// https://htmldom.dev/create-resizable-split-views/
//

document.addEventListener('DOMContentLoaded', function () {
    // Query the element
    const resizer = document.getElementById('window_resizer');
    const source_window = document.getElementById('source_window');
    const output_window = document.getElementById('output_window');
    // const source_window = resizer.previousElementSibling;
    // const output_window = resizer.nextElementSibling;

    // Source code box
    const source = document.getElementById('source');

    // Left window width hidden field
    const left_window_width = document.getElementById('left_window_width');

    // Load from localStorage
    source_window.style.width = load(source_window.id+"_width", "50vw");
    left_window_width.value = source_window.style.width;

    // The current position of mouse
    let x = 0;
    let y = 0;
    let leftWidth = 0;

    // Handle the mousedown event
    // that's triggered when user drags the resizer
    const mouseDownHandler = function (e) {
        // Get the current mouse position
        x = e.clientX;
        y = e.clientY;
        leftWidth = source_window.getBoundingClientRect().width;

        // Attach the listeners to `document`
        document.addEventListener('mousemove', mouseMoveHandler);
        document.addEventListener('mouseup', mouseUpHandler);
    };

    const mouseMoveHandler = function (e) {
        // How far the mouse has been moved
        const dx = e.clientX - x;
        const dy = e.clientY - y;

        const newLeftWidth = ((leftWidth + dx) * 100) / resizer.parentNode.getBoundingClientRect().width;
        source_window.style.width = `${newLeftWidth}%`;

        resizer.style.cursor = 'col-resize';
        document.body.style.cursor = 'col-resize';

        source_window.style.userSelect = 'none';
        source_window.style.pointerEvents = 'none';

        output_window.style.userSelect = 'none';
        output_window.style.pointerEvents = 'none';
    };

    const mouseUpHandler = function () {
        resizer.style.removeProperty('cursor');
        document.body.style.removeProperty('cursor');

        source_window.style.removeProperty('user-select');
        source_window.style.removeProperty('pointer-events');

        output_window.style.removeProperty('user-select');
        output_window.style.removeProperty('pointer-events');

        // Remove the handlers of `mousemove` and `mouseup`
        document.removeEventListener('mousemove', mouseMoveHandler);
        document.removeEventListener('mouseup', mouseUpHandler);

        // Store current left window width
        save(source_window.id+"_width", source_window.offsetWidth+"px");
        left_window_width.value = source_window.offsetWidth+"px";
    };

    // Attach the handler
    resizer.addEventListener('mousedown', mouseDownHandler);
});

function set_page_zoom() {
    var html = document.getElementsByTagName("html")[0];
    html.style.fontSize = 1;
}
