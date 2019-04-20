export function helpStart(_board) {
    return helpRequest('get_help_start', _board, "");
}

export function help(_board, _question) {
    return helpRequest('get_help', _board, _question);
}

export function helpEnd(_board) {
    return helpRequest('get_help_end', _board, "");
}

function helpRequest(address, _board, _question) {
    let result = new Promise((resolve, reject) => {
        fetch('http://helpermock.herokuapp.com/' + address, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ board: _board, question: _question || "" })
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                resolve(data);
            })
            .catch(function (error) {
                reject(error);
            });
    });
    return result;
}