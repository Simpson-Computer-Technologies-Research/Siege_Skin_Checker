// Windows + R (Run)
// Copy paste line below to enter unsecure google session
// chrome.exe --user-data-dir="C://Chrome dev session" --disable-web-security


// Function to append child
function _append(p, n) {
    p.appendChild(n);
    const e = document.getElementById("main");
    e.appendChild(p);
    e.style.textAlign = "center";
}

// Function to reset the "main" element's innerHTML
function _reset() {
    const f = document.getElementById("main");
    f.innerHTML = '';
}

// Main function
function main(){
    var name = document.getElementById('name').value;
    if (name.length > 2) {
        _reset()

        // My Heroku Api
        fetch(`https://r6-skins-api.herokuapp.com/skins/uplay/${name}`)
            .then(response => {return response.json();})
            .then(data => {
                for (var property in data["skins"]) {
                    try {
                        // Header
                        const categ_para = document.createElement("strong");
                        const categ_node = document.createTextNode(property + ": ");
                        categ_para.style.color = "white";

                        // Append child
                        _append(categ_para, categ_node);
                        
                        // Show the type of the skins
                        const skins_para = document.createElement("p");
                        const skins_node = document.createTextNode(data["skins"][property].join(', '));
                        _append(skins_para, skins_node);

                        // Show each skin
                        const NL_para = document.createElement("p");
                        const NL_node = document.createTextNode("‏‏‎ ‎");
                        _append(NL_para, NL_node);
                    }
                    catch(err) {
                        console.log(err);
                    }
                    
                }
            });
    }
}
