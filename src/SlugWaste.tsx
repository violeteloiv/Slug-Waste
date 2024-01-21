import React from 'react';
import logo from './logo.svg';
import './SlugWaste.css';
import {
  createBrowserRouter,
  RouterProvider
} from 'react-router-dom';

import Login from './pages/LogIn';
import Home from './pages/Home';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Login/>
  },
  {
    path: '/home',
    element: <Home/>
  }
]);

function SlugWaste() {
  return (
    <div>
      <RouterProvider router={router}/>
    </div>
  )
}

export default SlugWaste;
