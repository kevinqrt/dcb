"use client"
import React, {useEffect, useRef, useState } from 'react';
import DarkModeButton from './themehandler/darkmode';
import MessageInput from './messageinput';
import { buildMessages } from '../utils/utils';


const ChatContainer: React.FC = () => {
  const [messages, setMessages] = useState<Array<string>>([]);

  const messagesEndRef = useRef<null | HTMLDivElement>(null); 

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages]);

  return (
    <div className="flex flex-col h-[calc(100dvh)] h-screen">
      <div className='bg-1 dark:bg-1-dark'>
        <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight md:text-5xl lg:text-6xl dark:text-white text-white p-5">DocumentChatBot</h1>
        <DarkModeButton />
      </div>
      <div className="mt-auto overflow-auto">
        {buildMessages(messages)}
        <div ref={messagesEndRef} />
      </div>
      <div>{<MessageInput setMessages={setMessages} messages={messages}/>}</div>
    </div>
  );
}
export default ChatContainer;