import { Dispatch, SetStateAction } from "react";
import MessageAnswer from "../components/messageanswer";
import MessageQuestion from "../components/messagequestion";
import MessageWaiting from "../components/messagewaiting";

export const getAnswer = async (question: string, start_new_conversation: Boolean) => {

  const url: URL = new URL(`${process.env.NEXT_PUBLIC_API_URL}/chat/ask`);

  const response: Response = await fetch(url, {
    credentials: 'include',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ 
      "question": question, 
      "new_conversation": start_new_conversation 
    }),
  });

  return response;
}

export const askQuestion = async (
  setMessages: Dispatch<SetStateAction<string[]>>, 
  question: string, start_new_conversation: Boolean,
  onAnswer: (setMessages: Dispatch<SetStateAction<string[]>>, answer: string, new_conversation: Boolean) => any,
  onQuestion: (setMessages: Dispatch<SetStateAction<string[]>>, question: string) => any) => {

  onQuestion(setMessages, question);

  const response: Response = await getAnswer(question, start_new_conversation);

  if (response.ok) {
    const responseBody: { response: string, new_conversation: Boolean } = await response.json();
    onAnswer(setMessages, responseBody.response, responseBody.new_conversation);
  }

}

export const onAnswer = (setMessages: Dispatch<SetStateAction<string[]>>, answer: string, new_conversation: Boolean) => {
  if (new_conversation) {
    setMessages(messages => [messages.at(-1)!, answer]);
  } else {
    setMessages(messages => [...messages, answer]);
  }
}

export const onQuestion = (setMessages: Dispatch<SetStateAction<string[]>>, question: string) => {
  setMessages(messages => [...messages, question]);

}

export const buildMessages = (messages: Array<string>) => {
  let messageElements: JSX.Element[]
    = messages.map((message: string, index: number) => {
      if (index % 2 == 1) {
        return <MessageAnswer answer={message} key={index} />
      } else {
        return <MessageQuestion question={message} key={index} />
      }
    });
  if (messageElements.length % 2 == 1) {
    messageElements.push(<MessageWaiting key={"message_waiting"} />);
  }
  return messageElements;
}

export const start_new_conversation =  (messages: Array<string>) => {
  if (messages.length === 0){
    return true;
  } else {
    return false;
  }
}
