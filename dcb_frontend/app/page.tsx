"use client"
import MessageInput from './components/messageinput'
import ChatContainer from './components/chatcontainer'
import { useState } from 'react';
import { buildMessages } from './utils/utils';

export default function Home() {
  const [messages, setMessages] = useState<Array<string>>([]);
  
  return (
    <main>
      <ChatContainer input={<MessageInput setMessages={setMessages} messages={messages}/>}>
        {buildMessages(messages)}
      </ChatContainer>
    </main>
  )
}