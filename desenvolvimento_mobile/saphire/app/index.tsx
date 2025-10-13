import { router } from "expo-router";
import { useState } from "react";
import { ImageBackground, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

export default function Index() {
  const [isChecked, setCheck] = useState(false)
  return (
    <ImageBackground 
      source={require('../assets/images/ado_sword.jpg')} 
      style={style.backgroundImage} 
      resizeMode="cover"
    >
      <SafeAreaView style={style.container}>
        <View style={style.main_content}>
          <Text style={style.title}>Start a new social adventure</Text>
        </View>
        <View style={style.form}>
          <TouchableOpacity 
            style={style.button}
            onPress={() => router.push('/login')}
          >
            <Text style={style.text}>Sign In</Text>
          </TouchableOpacity>
          
          <TouchableOpacity 
            style={style.button}
            onPress={() => router.push('/register')}
          >
            <Text style={style.text}>Create Account</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    </ImageBackground>
  );
}


const style = StyleSheet.create({
  backgroundImage: {
    flex: 1,
    width: '100%',
    height: '100%',
  },
  container: {
    flex: 1,
  },
  main_content: {
    position: 'absolute',
    top: '30%',
    left: 0,
    right: 0,
    zIndex: 1,
    alignItems: 'center',
  },
  title:{
    fontSize:24,
    fontWeight: '900',
    color: '#00955cff',
    alignSelf: 'center',
  },
  form: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    height: '40%',
    backgroundColor:'rgba(70, 65, 65, 0.85)',
    padding: 40,
    gap: 20,
    justifyContent: 'center',
    alignItems: 'center',
    borderTopRightRadius: 90,
    borderTopLeftRadius: 20,
  },
  button: {
    backgroundColor: 'rgba(0, 0, 0, 0.7)',
    padding: 15,
    borderRadius: 12,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.3)',
    minWidth: 200,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  text: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
    textAlign: 'center'
  }
})