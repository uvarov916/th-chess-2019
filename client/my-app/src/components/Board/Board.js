import React from 'react';
import './Board.css';
import {figures} from "./constants";


export class Board extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      board: '',
    };
    this.editedCell = [];
    this.step = '';
    this.getFigures=this.getFigures.bind(this);
  }

  getFigures() {
    this.editedCell=[];
    let index;
    let fen = this.state.board.split(' ');
    let board = fen[0].split("/");
    for (let i = 0; i < board.length; i++) {
      let str = board[i].split("");
      for (let j = 0; j < str.length; j++) {
        if (isFinite(str[j])) {
          index = Number.parseInt(str[j]);
          while (index > 0) {
            this.editedCell.push('');
            index--;
          }
        } else {
          this.editedCell.push(str[j]);
        }
      }
    }
  }

  static getDerivedStateFromProps(props){
    return {board : props.fen};
  }

  render() {
    let cell = true;
    const items=[];
    this.getFigures();
    for (const[index,value] of this.editedCell.entries()) {
      if (index % 8 === 0) {cell = !cell;}
      if (value!== '') {
          if (cell) {
            cell = false;
            items.push(<div key = {index} className={value + ' figure + '}>
              <img src={figures[value]} className='figure + board_cell_darkolivegreen'/>
            </div>);
          } else {
            cell = true;
            items.push(<div key = {index} className={value + ' figure + '}>
              <img src={figures[value]} className='figure + board_cell_lime'/>
            </div>);
          }
      } else {
        if (cell) {
          cell = false;
          items.push(<div key={index} className='figure + board_cell_darkolivegreen'>
          </div>);
        } else {
          cell = true;
          items.push(<div key={index} className='figure + board_cell_lime'>
          </div>);
        }
      }
    }
    return (
          <div className='board'>
            {items}
          </div>
    );
  }
}


