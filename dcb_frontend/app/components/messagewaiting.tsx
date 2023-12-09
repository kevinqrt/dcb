const MessageWaiting: React.FC = () => {

  return (
    <>
      <div className="chat chat-start p-3">
        <div className="chat-bubble bg-4 dark:bg-1-dark flex gap-1">
          <div className="dark:bg-white bg-black rounded-full h-3 w-3 animate-bounce self-end">
          </div>
          <div className="dark:bg-white bg-black rounded-full h-4 w-4 animate-bounce self-end">
          </div>
          <div className="dark:bg-white bg-black rounded-full h-5 w-5 animate-bounce self-end">
          </div>
        </div>
      </div>
    </>
  );
};
export default MessageWaiting;