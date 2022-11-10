import {
    BrowserRouter as Router,
    Switch,
    Route
} from 'react-router-dom'

import Minesweeper from './Minesweeper'
import Jokes from './Jokes'
import App from './App'
import PageTemplate from './PageTemplate'

function ReactSite() {
  return (
    <div>
        <Router>
            <PageTemplate>
                <Switch>
                    <Route path='/' exact>
                    </Route>
                    <Route path='/minesweeper' exact>
                        <Minesweeper/>
                    </Route>
                    <Route path='/jokes' exact>
                        <Jokes/>
                    </Route>
                    <Route path='/login' exact>
                        <App/>                    
                    </Route>
                </Switch>
            </PageTemplate>
         </Router>
    </div>
  )
}

export default ReactSite