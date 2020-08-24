import React, { Component } from "react";

class Counter extends Component {
  constructor(props) {
    super(props);

    this.state = {
      count: 0,
    };
  }
  increment() {
    // this.setState({
    //   count: this.state.count + 1,
    // });
    this.setState((prevstate) => ({
      count: prevstate.count + 1,
    }));
  }
  decrement() {
    this.setState({
      count: this.state.count - 1,
    });
  }
  render() {
    return (
      <div>
        <h1> Count={this.state.count} </h1>
        <button onClick={() => this.increment()}>+</button>
        <button onClick={() => this.decrement()}>-</button>
      </div>
    );
  }
}

export default Counter;
