function getCurrentDate() {
    const currentDate = new Date();
    return "Last Sync: " + currentDate.getDate() + "/"
        + (currentDate.getMonth() + 1) + "/"
        + currentDate.getFullYear() + " @ "
        + currentDate.getHours() + ":"
        + currentDate.getMinutes() + ":"
        + currentDate.getSeconds();
}

function getSessions() {
    $.get({
        url: "http://localhost:22000/sessions?api_key=api123",
        success: function (result) {
            const tableBody = $("#sessionTableBody");
            tableBody.empty();
            $.each(result.sessions, function (index, item) {
                let row = `<tr>
                                <td>${item.registro}</td>
                                <td>${item.nome}</td>
                                <td>${item.email}</td>
                                <td>${item.tipo_usuario}</td>
                               </tr>`;
                tableBody.append(row);
            });
            $("#error").text('');
        },
        error: function (error) {
            $("#error").text('Error obtaining sessions');
            console.error(error);
        }
    });
    $("#info").text(getCurrentDate());
}

$(document).ready(function () {
    getSessions();
    setInterval(getSessions, 5000);
});