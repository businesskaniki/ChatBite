import { Routes, Route } from 'react-router-dom';
import Register from './components/auth/ Register';
import Login from './components/auth/Login';
import Home from './components/Home';
import Layout from './components/Layout';
import Missing from './components/missing/Missing';
import Unauthorized from './components/auth/ Unauthorized';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        {/* public routes */}
        <Route path="login" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route path="unauthorized" element={<Unauthorized />} />
        <Route path="/" element={<Home />} />
        {/* we want to protect these routes */}

        {/* catch all */}
        <Route path="*" element={<Missing />} />
      </Route>
    </Routes>
  );
}

export default App;
