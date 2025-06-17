//import logo from "./logo.svg";
import "./App.css";
import Crick from './components/Crick';

function App() {
  return (
    <div>
      <Crick target={200} totalOvers={10} />
      <br></br>
    </div>
  );
}

export default App;
