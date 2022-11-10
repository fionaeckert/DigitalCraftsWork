import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './components/App';
import BaseLayout from './components/layout/BaseLayout'
import { BrowserRouter as Router, Routes as Switch, Route } from 'react-router-dom'
import Forms from './components/Forms';
import FormsClass from './components/FormsClass'
import News from './components/News'
import ShoppingList from './components/ShoppingList';
import AddressBook from './components/AddressBook';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>

  <Router>
    <BaseLayout>
      <Switch>
        <Route path = "/" element={<App />} />
        <Route path = "/forms" element={<Forms />} />
        <Route path = "/formsclass" element={<FormsClass />} />        
        <Route path = "/news" element={<News />} />
        <Route path = "/shoppinglist" element={<ShoppingList />} />
        <Route path = "/addressbook" element={<AddressBook />} />
      </Switch>
    </BaseLayout>
  </Router>
  
  
  </React.StrictMode>
);

