import { BookOpen, Phone, Heart, Globe, Shield, Brain } from 'lucide-react';

const Resources = () => {
  const emergencyContacts = [
    { name: "National Suicide Prevention Lifeline", phone: "988", description: "Available 24/7. Languages: English, Spanish." },
    { name: "Crisis Text Line", phone: "Text HOME to 741741", description: "Connect with a volunteer Crisis Counselor 24/7, free, confidential." },
    { name: "The Trevor Project", phone: "1-866-488-7386", description: "Crisis intervention and suicide prevention for LGBTQ youth." }
  ];

  const infoCards = [
    {
      title: "How MindEase Works",
      icon: BookOpen,
      content: "MindEase uses a Natural Language Processing model trained on over 20,000 text samples to detect underlying emotional patterns in text. It can identify Joy, Sadness, Anger, Fear, Surprise, and Neutral states.",
      color: "text-blue-400",
      bg: "bg-blue-400/10",
      border: "border-blue-400/20"
    },
    {
      title: "Privacy First",
      icon: Shield,
      content: "Your conversations are processed in real-time and are not stored in our database. We believe in providing a safe, confidential space for emotional reflection.",
      color: "text-emerald-400",
      bg: "bg-emerald-400/10",
      border: "border-emerald-400/20"
    },
    {
      title: "AI Limitations",
      icon: Brain,
      content: "While our model has an 88% accuracy rate, it is an AI tool, not a human therapist. If you are experiencing a crisis, please use the emergency contacts provided on this page.",
      color: "text-purple-400",
      bg: "bg-purple-400/10",
      border: "border-purple-400/20"
    }
  ];

  return (
    <div className="flex-1 max-w-6xl mx-auto w-full p-4 sm:p-8">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-white mb-4">Support & Resources</h1>
        <p className="text-lg text-slate-400 max-w-2xl mx-auto">
          Information about the MindEase system and important emergency contacts if you need immediate human support.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Column: System Info */}
        <div className="lg:col-span-2 space-y-6">
          <h2 className="text-2xl font-semibold text-white mb-6 flex items-center gap-2">
            <Globe className="w-6 h-6 text-brand-400" />
            About the System
          </h2>
          
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            {infoCards.map((card, idx) => {
              const Icon = card.icon;
              return (
                <div key={idx} className={`glass-panel p-6 border ${card.border} hover:bg-white/5 transition-colors`}>
                  <div className={`w-12 h-12 rounded-xl ${card.bg} flex items-center justify-center mb-4`}>
                    <Icon className={`w-6 h-6 ${card.color}`} />
                  </div>
                  <h3 className="text-lg font-semibold text-white mb-2">{card.title}</h3>
                  <p className="text-slate-400 text-sm leading-relaxed">
                    {card.content}
                  </p>
                </div>
              );
            })}
          </div>
        </div>

        {/* Right Column: Emergency Contacts */}
        <div className="space-y-6">
          <h2 className="text-2xl font-semibold text-white mb-6 flex items-center gap-2">
            <Heart className="w-6 h-6 text-rose-400" />
            Emergency Help
          </h2>
          
          <div className="space-y-4">
            {emergencyContacts.map((contact, idx) => (
              <div key={idx} className="glass-panel p-6 border border-rose-500/20 bg-gradient-to-br from-rose-500/5 to-transparent relative overflow-hidden">
                <div className="absolute top-0 right-0 p-4 opacity-10">
                  <Phone className="w-16 h-16 text-rose-400" />
                </div>
                <h3 className="text-lg font-semibold text-white mb-1">{contact.name}</h3>
                <div className="text-2xl font-bold text-rose-400 mb-2">{contact.phone}</div>
                <p className="text-sm text-slate-400">{contact.description}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

// We need to import Shield and Brain at the top that were missed in the static definition above. Let's fix that inline or ignore and let Vite throw error? Wait, I will add it to the import.
export default Resources;
