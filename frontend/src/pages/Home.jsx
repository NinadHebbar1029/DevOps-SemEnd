import { ArrowRight, Activity, Brain, Shield, Sparkles } from 'lucide-react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="flex-1 flex flex-col items-center pt-20 px-4">
      {/* Hero Section */}
      <div className="max-w-4xl w-full text-center mb-20 animate-float">
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full glass-panel mb-8 border-brand-500/30">
          <Sparkles className="w-4 h-4 text-brand-400" />
          <span className="text-sm font-medium text-brand-200">AI-Powered Emotion Detection</span>
        </div>
        
        <h1 className="text-5xl md:text-7xl font-extrabold mb-6 tracking-tight text-white">
          Understand Your <br />
          <span className="text-gradient">Mental Well-being</span>
        </h1>
        
        <p className="text-xl text-slate-300 mb-10 max-w-2xl mx-auto leading-relaxed">
          MindEase provides a safe space to express your feelings. Our advanced AI model analyzes your text to help identify and track 6 distinct emotional states.
        </p>

        <Link 
          to="/chat" 
          className="inline-flex items-center gap-2 px-8 py-4 bg-brand-600 hover:bg-brand-500 text-white rounded-xl font-bold text-lg transition-all shadow-[0_0_40px_rgba(79,70,229,0.4)] hover:shadow-[0_0_60px_rgba(79,70,229,0.6)] transform hover:-translate-y-1"
        >
          Start Chatting
          <ArrowRight className="w-5 h-5" />
        </Link>
      </div>

      {/* Metrics Section */}
      <div className="max-w-5xl w-full grid grid-cols-1 md:grid-cols-3 gap-6 mb-20">
        <div className="glass-panel text-center p-8 relative overflow-hidden group">
          <div className="absolute inset-0 bg-gradient-to-br from-brand-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
          <Activity className="w-10 h-10 text-brand-400 mx-auto mb-4" />
          <div className="text-4xl font-bold text-white mb-2">6</div>
          <div className="text-sm font-medium text-slate-400 uppercase tracking-wider">Supported Emotions</div>
        </div>

        <div className="glass-panel text-center p-8 relative overflow-hidden group">
          <div className="absolute inset-0 bg-gradient-to-br from-purple-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
          <Brain className="w-10 h-10 text-purple-400 mx-auto mb-4" />
          <div className="text-4xl font-bold text-white mb-2">20K+</div>
          <div className="text-sm font-medium text-slate-400 uppercase tracking-wider">Dataset Size</div>
        </div>

        <div className="glass-panel text-center p-8 relative overflow-hidden group">
          <div className="absolute inset-0 bg-gradient-to-br from-emerald-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
          <Shield className="w-10 h-10 text-emerald-400 mx-auto mb-4" />
          <div className="text-4xl font-bold text-white mb-2">88%</div>
          <div className="text-sm font-medium text-slate-400 uppercase tracking-wider">Best Accuracy</div>
        </div>
      </div>
      
      {/* Background Orbs */}
      <div className="fixed top-20 left-20 w-96 h-96 bg-brand-600/20 rounded-full blur-[120px] -z-10 pointer-events-none" />
      <div className="fixed bottom-20 right-20 w-96 h-96 bg-purple-600/20 rounded-full blur-[120px] -z-10 pointer-events-none" />
    </div>
  );
};

export default Home;
