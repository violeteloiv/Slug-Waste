import React from 'react';
import logo from './logo.svg';
import './SlugWaste.css';
import {
  createBrowserRouter,
  RouterProvider
} from 'react-router-dom';

import Login from './pages/LogIn';
import Submission from './pages/Submission';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Login/>
  },
  {
    path: '/submission',
    element: <Submission/>
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
