
function populate() {
    console.log("loading data");
    let station_list = document.getElementById("station_list");
    let search_bar = document.getElementById("search_bar")
    let bus_stations = '';
    let load_message = document.createElement("h3");
    load_message.innerText = "Loading...";
    station_list?.appendChild(load_message);

    fetch('https://h4nmsf5uxc2kytzpco74ds5ody0mffge.lambda-url.us-west-2.on.aws/')
        .then(function (response) {
            return response.json();
        })
        .then(function (api_data) {

            bus_stations = api_data

            let route;
            for (let s in bus_stations) {
                const div = document.createElement("div")
                div.id = s
                div.className = "container"
                station_list?.appendChild(div)


                const h3 = document.createElement("h3")
                h3.textContent = s
                div?.appendChild(h3)

                for (let i in bus_stations[s]) {
                    route = bus_stations[s][i]
                    const p = document.createElement('p')
                    p.textContent = "route name: " + route['name'] + " edt: " + route['edt'] + " sdt: " + route['sdt']

                    if (route['edt'] !== route['sdt']){
                        p.className = "p-3 mb-2 bg-success text-dark"
                    } else {
                        p.className = "p-3 mb-2 bg-warning text-dark"
                    }
                    div.appendChild(p)
                }
                load_message.remove()
            }
        });

    search_bar.setAttribute("onkeyup", "filter();")

}

function filter() {

    let input, filter, content_div, subdivs;

    input = document.getElementById("search_bar");
    filter = input.value.toUpperCase();

    content_div = document.getElementById("station_list");
    subdivs = content_div.getElementsByTagName("div");
    for (let i in subdivs){
        let d = subdivs[i];

        if (d.id.toUpperCase().indexOf(filter) > -1){
            d.style.display = "";
        } else {
            d.style.display = "none";
        }
    }
}