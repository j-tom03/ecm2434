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
        .addEventListener("click", function (event) {
            event.stopPropagation(); // Prevent event propagation
            toggleVisibility("profileInfo");
        });

    document
        .getElementById("shopButton")
        .addEventListener("click", function (event) {
            event.stopPropagation(); // Prevent event propagation
            toggleVisibility("shopInfo");
        });

    // Add event listener to hide profile/shop div when clicking outside
    document.addEventListener("click", function (event) {
        const profileDiv = document.getElementById("profileInfo");
        const shopDiv = document.getElementById("shopInfo");
        if (!profileDiv.contains(event.target)) {
            profileDiv.style.display = "none";
        }
        if (!shopDiv.contains(event.target)) {
            shopDiv.style.display = "none";
        }
    });
});

function toggleVisibility(divId) {
    var div = document.getElementById(divId);
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}
