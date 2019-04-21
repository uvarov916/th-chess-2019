const HEROKU_URL = 'https://boardtsr.herokuapp.com/';
const SASHA_URL = 'http://10.54.32.205:8000/'
const LOCAL_URL = 'http://127.0.0.1:8000/'

export function init() {
    return boardRequest('init');
}

export function getBoard() {
    return boardRequest('get_board');
}

export function getSwapped(selectedCells) {
    let cells = [];
    selectedCells.forEach((element, index) => {
        if (element) {
            let whole = Math.floor(index / 8)
            let part = index - whole * 8;
            cells.push([whole, part])
        }
    });
    return swapRequest(cells);
}

function swapRequest(cells) {
    let result = new Promise((resolve, reject) => {
        fetch(LOCAL_URL + "swap", { 
            method : "POST", 
            headers : {
                'mode': 'no-cors',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ "cells": cells })
        })
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

function boardRequest(address) {
    let result = new Promise((resolve, reject) => {
        fetch(LOCAL_URL + address, { 
            method : "GET", 
            headers : {
                'mode': 'no-cors',
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