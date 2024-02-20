function create_grid(width, height) {
    const plot = document.getElementById('plot-container');
    for (let i = 0; i < width * height; i++) {
        const tile = document.createElement('div');
        tile.classList.add('tile');
        plot.appendChild(tile)
    }
}

function populate_t(tile_string) {
    const plot = document.getElementById('plot-container');
    const tiles = plot.childNodes;
    for (let i = 0; i < tile_string.length; i++) {
        if (tile_string[i] != '0') {
            tiles[i].textContent = tile_string[i];
        }
    }
}

