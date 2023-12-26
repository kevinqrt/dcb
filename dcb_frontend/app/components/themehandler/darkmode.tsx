"use client"
import { useState, useEffect } from 'react'
import { useTheme } from 'next-themes'
import { FaMoon, FaSun } from 'react-icons/fa'

const DarkModeButton = () => {
  const [mounted, setMounted] = useState(false)
  const { setTheme } = useTheme()
  const { resolvedTheme } = useTheme()

  useEffect(() => {
    setMounted(true)
  }, [])

  if (!mounted) {
    return null
  }

  return (
    <button className='absolute right-4 top-4' onClick={e => resolvedTheme === 'dark' ? setTheme('light') : setTheme('dark')}>
        {resolvedTheme === 'dark' ? <FaMoon /> : <FaSun />}
    </button>
  )
}

export default DarkModeButton