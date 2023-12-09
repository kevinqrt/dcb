import React, { ReactNode, useEffect, useRef } from 'react';
import DarkModeButton from './themehandler/darkmode';

interface ChatContainerProps {
  children: ReactNode;
  input: ReactNode;
}

const ChatContainer: React.FC<ChatContainerProps> = ({ children, input }) => {

  const messagesEndRef = useRef<null | HTMLDivElement>(null); 

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }

  useEffect(() => {
    scrollToBottom()
  }, [children]);

  return (
    <div className="flex flex-col h-screen">
      <div className='bg-1 dark:bg-1-dark'>
        <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight md:text-5xl lg:text-6xl dark:text-white text-white p-5">DocumentChatBot</h1>
        <DarkModeButton />
      </div>
      <div className="mt-auto overflow-auto">
        {children}
        <div ref={messagesEndRef} />
      </div>
      <div>{input}</div>
    </div>
  );
}
export default ChatContainer;