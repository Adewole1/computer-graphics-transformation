classdef Transform
    
    methods (Static)
        function [transform_list,transformations] = transform
            transform_list = [];
            keys = {'T', 'O', 'C', 'S', 'R'};
            values = {'Transform.translate', 'Transform.rotate', 'Transform.scale', 'Transform.shear', 'Transform.reflect'};
            transformations = containers.Map(keys, values);
            while 1 
                transformation = input('\nEnter the transformation(s) you want to do: \nIn the order you want to do them\nTranslate, rOtate, sCale, Shear, Reflect \nor Done when you are done or cLear to start again: \n', 's');
                if ismember(upper(transformation), keys)
                    transform_list = cat(1, transform_list, upper(transformation));
                elseif strcmpi(transformation, 'd')
                    if isempty(transform_list)
                        disp('\nYou have entered no transformation, try again.')
                        continue
                    else
                        break
                    end
                elseif strcmpi(transformation, 'l')
                    Transform.transform;
                else
                    disp('\nYou have entered an incorrect transformation, try again.')
                    continue
                end
            end
            transform_list = transform_list';
%             disp(transform_list)
%             class(transform_list)
%             Transform.point
        end
        
        function [transform_list, transformations, coordinates] = point
            if exist('transform_list','var')
                % do nothing
            else
                [transform_list, transformations] = Transform.transform;
%             disp(strlength(transform_list))
            coordinates = [];
            while 1
    %                coord = [];
                coord_in = input('\nEnter the coordinates of the shape in the format (x,y) or D when done or cLear to start again: \n', 's');
                if strlength(coord_in) == 0
                    disp('You have entered no coordinates, try again.')
                    continue
                else
                    if strcmpi(coord_in,'d')
                        if (length(coordinates(:, 1)) == 1) && (strlength(transform_list) == 1) && (strcmpi(transform_list(1), 't'))
                            % do nothing
                            break
                        % elseif strlength(transform_list) == 1
                        %     % do nothing
                        %     break
                        % elseif strcmpi(transform_list(1), 't')
                        %     % do nothing
                        %     break
                        elseif length(coordinates(:, 1)) == 2
                            % do nothing
                            break
                        elseif length(coordinates(:, 1)) > 2
                            % do nothing
                            break
                        else
                            disp('\nCannot transform a point, \nCheck transformation and points.')
                            continue
    %                        Transform.check_coordinates
                        end
                    elseif strcmpi(coord_in,'l')
                        Transform.point
                    elseif strcmpi(coord_in,'s')
                        Transform.transform
                    elseif length(str2num(coord_in)) < 2 || length(str2num(coord_in)) > 3
                        disp('This program can only work on 2D and 3D objects, try again.')
                        continue
                    else
                        try
                            coord_ = str2num(coord_in);
                            if isempty(coord_)
                                disp('You have entered a letter instead of numbers as coordinates')
                                continue
                            end
                            coord_ = cat(1, coord_', 1);
                            coordinates = cat(1, coordinates, coord_');
                            
                        catch ME
                            switch ME.identifier
                                case 'MATLAB:catenate:dimensionMismatch'
                                    disp('The dimensions are not consistent, try again')
                                    Transform.point
                                    break
                                otherwise
                                    rethrow(ME)
%                                     continue
                            end
                            
    %                            disp('An error occured with the coordinates, try again.')
                            
                        end
                    end
                end
            end
            disp('Coordinates are homogenous')
%             disp(coordinates)
            end
        end
        
        function M1 = transform_coordinates
            [transform_list, transformations, coordinates] = Transform.point;
            keys = {'T', 'O', 'C', 'S', 'R'};
            values = {'Translate', 'Rotate', 'Scale', 'Shear', 'Reflect'};
            transformations_list = containers.Map(keys, values);
            M = coordinates;
            M1 = M;
            transformed_list = [];
            for i = transform_list()
                Tx = '';
                Ty = '';
                M3 = str2func(transformations(i));
                if upper(i) == 'T'
                    M3 = M3(M1, Tx, Ty);
                    M1 = M1*M3;
                elseif upper(i) == 'O'
                    [M3, rot, cord] = M3(M1);
                    if rot == '1'
                        disp(cord)
                        Tx = cord(1);
                        Ty = cord(2); 
                        M4 = Transform.translate(M1, Tx, Ty);
                        % disp(M4)
                        M2 = M1*M4;
                        % disp(M2)
                        M2 = M2*M3;
                        % disp(M2)
                        Tx = -cord(1);
                        Ty = -cord(2);
                        M5 = Transform.translate(M1, Tx, Ty);
                        % disp(M5)
                        M1 = M2*M5;
                        % disp(M1)
                    else
                        M1 = M1*M3;
                    end
                else
                    M3 = M3(M1);
                    M1 = M1*M3;
                end
                transformed_list = cat(1, transformed_list, M3);
                
            end
            if length(transform_list) == 1
                disp('\nYour transformation is: '), disp(transformations_list(transform_list(1)));
                
            else
                disp('\nYour transformations are: \n')
                for trans = transform_list
                    disp(trans)
%                     result = find(axes==axis);
%                     disp(transformations_list(transform_list(trans)))
                end
            end
            disp('\nYour coordinates are: \n')
            disp(M)
            disp('\nYour new coordinates after transformation are: \n')
            disp(M1)
            disp(transformed_list)
        end
        
        function T = translate(M1, Tx, Ty, Tz)
            % disp('Translate function')
            if length(M1(1, :)) == 3
                T = eye(3);
                if isempty(Tx) || isempty(Ty)
                    Tx = input("Enter the translation in x-direction: \n", 's');
                    Ty = input("Enter the translation in y-direction: \n", 's');
                    if (isempty(str2num(Tx))) || (isempty(str2num(Tx)))
                        disp('You have entered a letter instead of an integer')
                        Transform.translate
                    else
                        T(3, 1) = str2double(Tx);
                        T(3, 2) = str2double(Ty);
                    end
                else
                    T(3, 1) = Tx;
                    T(3, 2) = Ty;
                end
            else
                T = eye(4);
                if Tx == '' %#ok<*BDSCA>
                    Tx = input("Enter the translation in x-direction: \n", 's');
                    Ty = input("Enter the translation in y-direction: \n", 's');
                    Tz = input("Enter the translation in z-direction: \n", 's');
                    if (isempty(str2num(Tx))) || (isempty(str2num(Tx))) || (isempty(str2num(Tz)))
                        disp('You have entered a letter instead of an integer')
                        Transform.translate
                    else
                        T(4, 1) = str2double(Tx);
                        T(4, 2) = str2double(Ty);
                        T(4, 3) = str2double(Tz);
                    end
                else
                    T(4, 1) = str2double(Tx);
                    T(4, 2) = str2double(Ty);
%                     T(4, 3) = str2double(Tz);
                end
            end
%           disp(T)
        end

        function [O, rot, cord] = rotate(M1)
            tita = input('\nEnter the angle of rotation: \n(If clockwise, add a negative before the angle.) \n','s');
            try
                tita = str2num(tita);
                costita = cos(deg2rad(tita));
                sintita = sin(deg2rad(tita));
                if length(M1(1, :)) == 3
                    if (isempty(tita))
                        disp('You have entered a letter instead of an integer')
                        Transform.rotate
                    else
                        rot = input('\nDo you want to rotate about 1.an arbitrary Point 2.An Origin? \n' , 's');
%                         rot = upper(rot);
                        O = eye(3);
                        O(1,1) = costita;
                        O(2,2) = costita;
                        O(1,2) = sintita;
                        O(2,1) = -sintita;

                        if rot == '1'
                            cord = input('\nEnter the arbitrary point to rotate about as x,y: \n', 's');
                            cord = str2num(cord);
                            disp(cord)
                        else
                            cord =[];
                        end
                    end
                else
                    if (isempty(tita))
                        disp('You have entered a letter instead of an integer')
                        Transform.rotate
                    else
                        O = eye(4);
                        axis = input('Enter axis of rotation 1.X 2.Y 3.Z): \n', 's');
%                         axis = upper(axis);
                        if axis == '1'
                            O(2,2) = costita;
                            O(3,3) = costita;
                            O(2,3) = sintita;
                            O(3,2) = -sintita;
                        elseif axis == '2'
                            O(1,1) = costita;
                            O(3,3) = costita;
                            O(3,1) = sintita;
                            O(1,3) = -sintita;
                        elseif axis == '3'
                            O(1,1) = costita;
                            O(2,2) = costita;
                            O(1,2) = sintita;
                            O(2,1) = -sintita;
                        end
                    end
                end
                
            catch
                disp('An error occurred, try again.')
                [O, rot, cord] = Transform.rotate(M1);
            end
            
            % disp('Rotate function')
        end

        function C = scale(M1)
%             disp(M1)
            try
                if length(M1(1, :)) == 3
                    C = eye(3);
                    Cx = input('Enter the scale size in x-direction: \n', 's');
                    Cy = input('Enter the scale size in y-direction: \n', 's');
                    Cx = str2num(Cx);
                    Cy = str2num(Cy);
                    if (isempty(Cx)) || (isempty(Cy))
                        disp('You have entered a letter instead of an integer')
                        Transform.scale
                    else
                        C(1, 1) = Cx;
                        C(2, 2) = Cy;
                    end
                else
                    C = eye(4);
                    Cx = input('Enter the scale size in x-direction: \n', 's');
                    Cy = input('Enter the scale size in y-direction: \n', 's');
                    Cz = input('Enter the scale size in z-direction: \n', 's');
                    Cx = str2num(Cx);
                    Cy = str2num(Cy);
                    Cz = str2num(Cz);
                    if (isempty(Cx)) || (isempty(Cy)) || (isempty(Cz))
                        disp('You have entered a letter instead of an integer')
                        Transform.scale
                    else
                        C(1, 1) = Cx;
                        C(2, 2) = Cy;
                        C(3, 3) = Cz;
                    end
                end
            catch
                disp('An error occurred, try again.')
                C = scale(M1);
            end
            % disp('Scale function')
        end

        function S = shear(M1)
            try
                if length(M1(1, :)) == 3
                    S = eye(3);
                    disp(S)
                    sh = input('\nEnter the shear parameter: \n', 's');
                    axis = input('\nEnter the direction of shear 1.Y 2.X: \n', 's');
                    rel = input('\nIs the shear Relative to another line? 1.Relative 2.No: \n', 's');
%                     rel = upper(rel);
%                     axis = upper(axis);
                    sh = str2num(sh);
%                     disp(sh)
                    if (isempty(sh))
                        disp('You have entered a letter instead of an integer')
                        Transform.shear
                    else
                        if rel == '1'
                            rel_para = input('Enter line parameter: \n', 's');
                            rel_para = str2num(rel_para);
                            disp(rel_para)
                            if (isempty(rel_para))
                                disp('You have entered a letter instead of an integer')
                                Transform.shear
                            else
                                if axis == '1'
                                    S(3, 2) = (-sh)*(rel_para);
                                elseif axis == '2'
                                    S(3, 1) = (-sh)*(rel_para);
                                end
                            end
                        elseif rel == '2'
                            % Do nothing
                        end

                        if axis == '1'
                            S(1, 2) = sh;
                        elseif axis == '2'
                            S(2, 1) = sh;
                        end
                    end
                else
                    S = eye(4);
                    axis = input('\nEnter the direction of shear (y or x or z): \n', 's');
                    axes = ['X' 'Y' 'Z'];
                    axis = upper(axis);
                    result = find(axes==axis);
                    axes(result) = ''; %#ok<FNDSB>
                    sh1 = input('Enter the shear in %s-direction', axes(1), 's');
                    sh2 = input('Enter the shear in %s-direction', axes(2), 's');
                    sh1 = str2num(sh1); %#ok<*ST2NM>
                    sh2 = str2num(sh2);
                    if (isempty(sh1)) || (isempty(sh2))
                        disp('You have entered a letter instead of an integer')
                        Transform.shear
                    else
                        if axis == 'X'
                            S(1, 2) = sh1;
                            S(1, 3) = sh2;
                        elseif axis == 'Y'
                            S(2, 1) = sh1;
                            S(2, 3) = sh2;
                        elseif axis == 'Z'
                            S(3, 1) = sh1;
                            S(3, 2) = sh2;
                        end
                    end
                end
            catch
                disp('An error occurred, try again.')
                S = Transform.shear(M1);
            end
        end

        function R = reflect(M1)
            try
                if length(M1(1, :)) == 3
                    R = eye(3);
                    axis = input('Enter the axis to reflect about (1.X 2.Y 3.Origin 4.Line):\n', 's');
                    axis = upper(axis);
                    if axis == '1'
                        R(2, 2) = -1;
                    elseif axis == '2'
                        R(1, 1) = -1;
                    elseif axis == '3'
                        R(2, 2) = -1;
                        R(1, 1) = -1;
                    elseif axis == '4'
                        ref = input('Enter the axis of the line to reflect 1.X 2.Y:\n', 's');
                        ref = upper(ref);
                        if ref == '1'
                            R(1, 1) = 0;
                            R(2, 2) = 0;
                            R(1, 2) = 1;
                            R(2, 1) = 1;
                        elseif ref == '2'
                            R(1, 1) = 0;
                            R(2, 2) = 0;
                            R(1, 2) = -1;
                            R(2, 1) = -1;
                        end
                    end
                else
                    R = eye(4);
                    plane = input('Enter the plane to reflect about (1.XY, 2.XZ, 3.YZ):\n', 's');
                    if plane == '1'
                        R(3, 3) = -1;
                    elseif plane == '2'
                        R(2, 2) = -1;
                    elseif plane == '3'
                        R(3, 3) = -1;
                    end
                end
            catch
                disp('An error occurred, try again.')
                R = reflect(M1);
            end
            % disp('Reflect function')
        end
        
    end
    
end