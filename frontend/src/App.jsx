import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import ChatDashboard from './pages/ChatDashboard';
import Resources from './pages/Resources';

function App() {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <main className="flex-1 flex flex-col">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/chat" element={<ChatDashboard />} />
          <Route path="/resources" element={<Resources />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
