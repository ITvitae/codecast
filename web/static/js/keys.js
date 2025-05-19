// Event Listeners
document.addEventListener('keydown', mods_pressed);
document.addEventListener('keyup', mods_released);
function mods_pressed() {
    if ( event.ctrlKey ){
        switch (event.key) {
        case 'r':
            event.preventDefault();
            run();
        default:
            match = false;
        }
    }
}

function mods_released() {
}
