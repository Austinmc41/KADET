import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {
    render(){
        return (
            <div className="App">
            
                <form name="formFiltre" id="formFiltre" method="post">
                    <div class="form-inline">
                        <div class="form-group ">
                          <input type="hidden" name="nav" value="1" />
                          <label for="rf_numero" class="col-form-label sr-only">Rotational Type</label>
                          <input type="text" name="rotationtype" id="rf_numero" class="form-control mb-2 mr-sm-2" placeholder="Rotational Type" value="" />
                        </div>
                        <div class="form-group">
                          <label for="rf_client" class="form-label sr-only">Number</label>
                          <input type="text" name="preset" id="rf_client" class="form-control mb-2 mr-sm-2" placeholder="Value" value="" />
                        </div>
                    </div> 
                </form>

            </div>
        );
    }
    
}

export default App;
