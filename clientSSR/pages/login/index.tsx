import * as React from 'react'
import { NextPage } from 'next'
import Login from '../../components/login&register/Login'
import Layout from '../../components/Layout'

const LoginPage: NextPage = () => (
  <Layout>
    <Login />
  </Layout>
)

export default LoginPage
