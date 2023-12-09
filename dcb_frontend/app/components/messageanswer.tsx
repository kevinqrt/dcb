interface MessageAnswerProps {
    answer: string;
}

const MessageAnswer: React.FC<MessageAnswerProps> = ({ answer }) => {

  return (
    <>
      <div className="chat chat-start p-3">
        <div className="chat-bubble break-words bg-4 dark:bg-1-dark">
          <p className="text-black dark:text-gray-200 dark:bg-1-dark">{answer}</p>
        </div>
      </div>
    </>
  );
};
export default MessageAnswer;