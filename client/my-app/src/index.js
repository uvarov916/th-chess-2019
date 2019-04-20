import React from 'react';
import  {render} from 'react-dom';
import {BoardController} from './components/BoardController/BoardController';
import './components/src.css';


let appElement = document.getElementById('root');

const renderApp = () => {
    render(
        <BoardController/>,
        appElement
    );
};

renderApp();
