import {View, Text, Alert, Button} from 'react-native';
import { style } from '../styles/index_container';

export default function Index(){
    function CallMe(){
        Alert.alert('fui pressionado!')
    }

    return(
        <View style={style.container}>
            <Text style={style.text}>texto aleatorio</Text>
            <Button title='exploda' onPress={CallMe}/>
        </View>
    )
}