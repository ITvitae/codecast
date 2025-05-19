// Should add try except here with fallback to session storage
function save(id, value){
    localStorage.setItem(id, value);
}

function load(id, def='None'){
    if (!localStorage.getItem(id)) {
        return def;
    }
    return localStorage.getItem(id);
}

function save_source(){
    save(source.id, source.value);
}
