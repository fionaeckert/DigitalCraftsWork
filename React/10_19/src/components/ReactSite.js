import {
    BrowserRouter as Router,
    Switch,
    Route
} from 'react-router-dom'

import PageTemplate from './PageTemplate'
import Contact from './Contact'
import Tictactoe from './Tictactoe'
import Tarot from './Tarot'
import Login from './Login'
import './ReactSite.css'
import Logout from './Logout'
import Home from './Home'

function ReactSite() {
  return (
    <div>
        <Router>
            <PageTemplate>
                <Switch>
                    <Route path='/' exact>
                        <Home/>
                    </Route>
                    <Route path='/contact' exact>
                        <Contact/>
                    </Route>
                    <Route path='/tictactoe' exact>
                        <Tictactoe/>
                    </Route>
                    <Route path='/tarot' exact>
                        <Tarot/>                    
                    </Route>
                    <Route path='/login' exact>
                        <Login/>                    
                    </Route>
                    <Route path='/logout' exact>
                        <Logout/>                    
                    </Route>
                </Switch>
            </PageTemplate>
         </Router>
    </div>
  )
}

export default ReactSite