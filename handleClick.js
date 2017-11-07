$(document).ready(() => {
    const streamThis = (e) => {
        e.preventDefault();
        $.get( "http://127.0.0.1:5000/button-click", ( data, err ) => {
            console.log(data, err);
        })
    }

    document.getElementById("button").onclick = streamThis
})