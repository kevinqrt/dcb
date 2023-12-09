"use client"
import React, { useState, ChangeEvent, KeyboardEvent, SetStateAction, Dispatch } from 'react';
import { IoSend } from "react-icons/io5";
import { askQuestion, onAnswer, onQuestion, start_new_conversation } from '../utils/utils';

interface MessageInputProps {
  messages: Array<string>;
  setMessages: Dispatch<SetStateAction<string[]>>;
}

const MessageInput: React.FC<MessageInputProps> = ({ messages, setMessages }) => {
  const [message, setMessage] = useState<string>('');

  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    setMessage(e.target.value);
  };

  const handleSendMessage = () => {
    if (message.trim() !== '') {
      askQuestion(setMessages, message, start_new_conversation(messages) ,onAnswer, onQuestion);
      setMessage('');
    }
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div className="bg-transparent flex w-screen p-2">
      <input
        type="text"
        placeholder="Ask a question..."
        value={message}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        className='text-black dark:text-white w-full rounded-md border-2 dark:bg-1-dark dark:border-3-dark border-5 bg-2 pl-2 placeholder-gray-400'
      />
      <button onClick={handleSendMessage}
        className='max-w-fit p-2 cursor-pointer'>
        <IoSend />
      </button>
    </div>
  );
};

export default MessageInput;
