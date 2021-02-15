import logo from './logo.svg';
import './App.css';

//imports suggested from geeksforgeeks article
import React from 'react';
import axios from 'axios'; 

//As of now, I'm not quite exactly sure what "type" is so be aware that "type" may not be the optimal name for whatever it represents

class App extends React.Component {
    
    
    state = { 
        TypeAmounts : [], 
    } 

    componentDidMount() { 

        let data ; 

        axios.get('http://localhost:8000/scheduler/') 
        .then(res => { 
            data = res.data; 
            this.setState({ 
                TypeAmounts : data     
            }); 
        }) 
        .catch(err => {}) 
    } 

    //This render function currently is our last working good. I'm trying to implement something that actually takes in data from our model, but I'm having immense difficulty doing so.
    render() {  
        return( 
            <div> 

                <h1>test test hello?</h1> 

            </div>
        );  
    }  

    //render() { 
        //return( 
            //<div> 
                //{this.state.TypeAmounts.map((TypeAmount, id) =>  ( 
                        //<div key={id}> 
                        //<div > 
                              //<div > 
                                    //<h1>{TypeAmount.TypeAmount} </h1> 
                                    //<footer >--- by 
                                    //<cite title="Source Title"> 
                                    //{TypeAmount.RotationType}</cite> 
                                    //</footer> 
                              //</div> 
                        //</div> 
                        //</div> 
                    //) 
                //)} 
            //</div> 
        //); 
    //} 
    
  
}

export default App;
