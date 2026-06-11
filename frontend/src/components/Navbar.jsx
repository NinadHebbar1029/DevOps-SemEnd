import { Link, useLocation } from 'react-router-dom';
import { Brain, MessageSquare, BookOpen, Home } from 'lucide-react';

const Navbar = () => {
  const location = useLocation();

  const navItems = [
    { path: '/', label: 'Home', icon: Home },
    { path: '/chat', label: 'Dashboard', icon: MessageSquare },
    { path: '/resources', label: 'Resources', icon: BookOpen },
  ];

  return (
    <nav className="glass-nav sticky top-0 z-50 px-6 py-4">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <Link to="/" className="flex items-center gap-2 group">
          <div className="p-2 bg-brand-500/20 rounded-xl group-hover:bg-brand-500/30 transition-colors">
            <Brain className="w-6 h-6 text-brand-400" />
          </div>
          <span className="text-xl font-bold text-white tracking-tight">MindEase AI</span>
        </Link>
        
        <div className="flex gap-2">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;
            
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all duration-300 ${
                  isActive 
                    ? 'bg-brand-500/20 text-brand-300' 
                    : 'text-slate-300 hover:text-white hover:bg-white/5'
                }`}
              >
                <Icon className="w-4 h-4" />
                <span className="hidden sm:block font-medium">{item.label}</span>
              </Link>
            );
          })}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
