export function init() {
    return boardRequest('init');
}

export function getBoard() {
    return boardRequest('get_board');
}

function boardRequest(address) {
    let result = new Promise((resolve, reject) => {
        fetch('https://boardtsr.herokuapp.com/' + address, { 
            method : "GET", 
            headers : {
                'Content-Type': 'application/json'
            }})
            .then(function (response) {
                return response.json()
            })
            .then(function (data) {
                resolve(data)
            })
            .catch(function (error) {
                reject(error);
            });
    });
    return result;
}