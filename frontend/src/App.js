import React from 'react';
import Criteria from "./components/criterion.component";
import One from "./components/one.component";
import Two from "./components/two.component";
import Three from "./components/three.component";

class App extends React.Component {  
    render() {  
        return( 
            <div>
                <h1 className="text-uppercase text-center my-4">Resident Scheduler app</h1>
                <div>
                    <React.Fragment>
                        <Criteria />
                    </React.Fragment>
                </div>
            </div>
        );
    }  
}  
export default App;