import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";
import Dealers from './components/Dealers/Dealers';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPanel />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dealers" element={<Dealers />} />
      </Routes>
    </Router>
  );
}

export default App;
