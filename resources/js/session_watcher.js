function getSessions() {
    $.get({
        url: "http://localhost:22000/sessions",
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
        },
        error: function (error) {
            console.log(`Error ${error}`);
        }
    });
}

$(document).ready(function () {
    getSessions();
    setInterval(getSessions, 5000);
});