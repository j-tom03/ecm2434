function create_grid(width, height) {
    const plot = document.getElementById("plot-container");
    for (let i = 0; i < width * height; i++) {
        const tile = document.createElement("div");
        tile.classList.add("tile");
        plot.appendChild(tile);
    }
}

function populate_t(tile_string) {
    const plot = document.getElementById("plot-container");
    const tiles = plot.childNodes;
    for (let i = 0; i < tile_string.length; i++) {
        if (tile_string[i] != "0") {
            tiles[i].textContent = tile_string[i];
        }
    }
}

document.addEventListener("DOMContentLoaded", function () {
    document
        .getElementById("profileButton")
        .addEventListener("click", function () {
            var profileInfoDiv = document.getElementById("profileInfo");
            if (profileInfoDiv.style.display === "none") {
                profileInfoDiv.style.display = "block";
            } else {
                profileInfoDiv.style.display = "none";
            }
        });
    document
        .getElementById("shopButton")
        .addEventListener("click", function () {
            var shopInfoDiv = document.getElementById("shopInfo");
            if (shopInfoDiv.style.display === "none") {
                shopInfoDiv.style.display = "block";
            } else {
                shopInfoDiv.style.display = "none";
            }
        });
});
