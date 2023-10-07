import './App.css';
import NavComp from './components/nav';
import backgroundVideo from './media/vid2.mp4'
import FooterComp from './components/footer';
import Nav2 from './components/nav2';
import Home from './components/home';
import Contact from './components/contact';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div>
    <Nav2/>
    <video autoPlay loop muted id='video'>
     <source src={backgroundVideo}/>
    </video>
    <FooterComp/>
    </div>
  );

}

export default App;
