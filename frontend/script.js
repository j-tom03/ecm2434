var recent_tile;

function create_grid(width, height) {
    const plot = document.getElementById("plot-container");
    for (let i = 0; i < width * height; i++) {
        const tile = document.createElement("div");
        tile.classList.add("tile");
        // make clickable:
        tile.setAttribute("data-index", i); // store index.
        tile.addEventListener("click", tileClickHandler); // add click event.
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

    document.getElementById("flower").addEventListener("click", purchase);
    document.getElementById("tree").addEventListener("click", purchase);
    document.getElementById("grass").addEventListener("click", purchase);
});

function toggleVisibility(divId) {
    var div = document.getElementById(divId);
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function tileClickHandler(event) {
    // get the index of the clicked tile.
    const index = event.target.getAttribute("data-index");
    event.stopPropagation();
    toggleVisibility("shopInfo");
    recent_tile = index;
    console.log("Tile index", index, " clicked.");
}

function purchase(event) {
    event.stopPropagation();

    const tile = get_tile(recent_tile);
    let cost = 0;

    if (event.target.id === "flower") {
        cost = 20;
        if (balance >= cost) {
            tile.textContent = "F";
            tile.style.backgroundColor = "pink";
            update_balance(cost, "subtract");
            toggleVisibility("shopInfo");
        } else {
            alert(
                "Insufficient funds. You need at least 20 coins to purchase this item."
            );
        }
    } else if (event.target.id === "tree") {
        cost = 40;
        if (balance >= cost) {
            tile.textContent = "T";
            tile.style.backgroundColor = "green";
            update_balance(cost, "subtract");
            toggleVisibility("shopInfo");
        } else {
            alert(
                "Insufficient funds. You need at least 40 coins to purchase this item."
            );
        }
    } else if (event.target.id === "grass") {
        cost = 10;
        if (balance >= cost) {
            tile.textContent = "G";
            tile.style.backgroundColor = "lightgreen";
            update_balance(cost, "subtract");
            toggleVisibility("shopInfo");
        } else {
            alert(
                "Insufficient funds. You need at least 10 coins to purchase this item."
            );
        }
    }
}

function get_tile(index) {
    const plot_cont = document.getElementById("plot-container");
    const tiles = plot_cont.childNodes;

    if (index >= 0 && index < tiles.length) {
        return tiles[index];
    } else {
        console.error("Invalid tile index:", index);
        return null;
    }
}

document.addEventListener("DOMContentLoaded", function () {
    var bottomBarButton = document.getElementById("bottomBarButton");
    var bottomBarContent = document.getElementById("bottomBarContent");
    var bottomBar = document.getElementById("bottomBar");

    bottomBarButton.addEventListener("click", function () {
        if (bottomBarContent.style.display === "none") {
            bottomBarContent.style.display = "block";
            bottomBarButton.innerHTML = "&#8595;"; // Change arrow direction
            bottomBar.classList.add("open"); // Add 'open' class
        } else {
            bottomBarContent.style.display = "none";
            bottomBarButton.innerHTML = "&#8593;"; // Change arrow direction
            bottomBar.classList.remove("open"); // Remove 'open' class
        }
    });
});
