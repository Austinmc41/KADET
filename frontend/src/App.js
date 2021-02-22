import React from 'react';
import Criteria from "./components/criterion.component";

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